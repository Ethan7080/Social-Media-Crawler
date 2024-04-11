import asyncio
import csv
import json
import os
import pathlib
from typing import Dict

import aiofiles
from tortoise.contrib.pydantic import pydantic_model_creator

from config.base_config import KEYWORDS
from base.base_crawler import AbstractStore
from tools import utils
from var import crawler_type_var

class XhsTxtStoreImplement(AbstractStore):
    def __init__(self):
        self.file_path : str = "data/xhs"
    async def store_content(self, content_item: Dict):
        # Check if the like count is greater than 100 before storing
        if int(content_item.get('liked_count', 0)) > int(100):
            await self._write_to_file(self._format_content_item(content_item), 'content')

    async def store_comment(self, comment_item: Dict):
          # Increment the counter when storing comment
        formatted_comment = self._format_comment_item(comment_item)
        await self._write_to_file(formatted_comment, 'comment')

    async def _write_to_file(self, data: str, data_type: str):
        # Create a unique filename for each entry
        #filename = f"{crawler_type_var.get()}_{data_type}_{utils.get_current_date()}_{KEYWORDS}.txt"
        filename = "output.txt"
        full_path = f"{self.file_path}/{filename}"
        # Write the formatted data to the text file asynchronously
        async with aiofiles.open(full_path, 'a', encoding='utf-8') as file:
            await file.write(str(data) + '\n\n')  # Ensure each entry is separated by a new line

    def _format_content_item(self, item: Dict) -> str:
        formatted_lines = [
            f"Type: {item.get('type', 'N/A')}",
            f"Title: {item.get('title', 'N/A')}",
            f"Description: {item.get('desc', 'N/A')}",
            f"Nickname: {item.get('nickname', 'N/A')}",
            f"Liked Count: {item.get('liked_count', 'N/A')}",
            f"Collected Count: {item.get('collected_count', 'N/A')}",
            f"Comment Count: {item.get('comment_count', 'N/A')}",
            f"Share Count: {item.get('share_count', 'N/A')}",
            f"Last Modify Timestamp: {item.get('last_modify_ts', 'N/A')}",
            f"Note URL: {item.get('note_url', 'N/A')}"
        ]
        return '\n'.join(formatted_lines)

    def _format_comment_item(self, item: Dict) -> str:
        # Generate a string representation of the comment item
        formatted_lines = [
            f"Comment Number: {self.post_counter}",
            f"Note ID: {item.get('note_id', 'N/A')}",
            f"Create Time: {item.get('create_time', 'N/A')}",
            f"IP Location: {item.get('ip_location', 'N/A')}",
            f"Content: {item.get('content', 'N/A')}",
            f"Nickname: {item.get('nickname', 'N/A')}",
            f"Sub Comment Count: {item.get('sub_comment_count', 'N/A')}",
            f"Last Modify Timestamp: {item.get('last_modify_ts', 'N/A')}"
        ]
        return '\n'.join(formatted_lines)
class XhsCsvStoreImplement(AbstractStore):
    csv_store_path: str = "data/xhs"

    def make_save_file_name(self, store_type: str) -> str:
        """
        make save file name by store type
        Args:
            store_type: contents or comments

        Returns: eg: data/xhs/search_comments_20240114.csv ...

        """
        return f"{self.csv_store_path}/{crawler_type_var.get()}_{store_type}_{utils.get_current_date()}.csv"

    async def save_data_to_csv(self, save_item: Dict, store_type: str):
        """
        Below is a simple way to save it in CSV format.
        Args:
            save_item:  save content dict info
            store_type: Save type contains content and comments（contents | comments）

        Returns: no returns

        """
        pathlib.Path(self.csv_store_path).mkdir(parents=True, exist_ok=True)
        save_file_name = self.make_save_file_name(store_type=store_type)
        async with aiofiles.open(save_file_name, mode='a+', encoding="utf-8-sig", newline="") as f:
            f.fileno()
            writer = csv.writer(f)
            if await f.tell() == 0:
                await writer.writerow(save_item.keys())
            await writer.writerow(save_item.values())

    async def store_content(self, content_item: Dict):
        """
        Xiaohongshu content CSV storage implementation
        Args:
            content_item: note item dict

        Returns:

        """
        def meets_criteria(item):
            # Example criteria: Check if 'liked_count' is greater than 20 and comment_count is greater than 10
            return int(item.get('liked_count', 0)) > 20 and int(item.get('comment_count', 0)) > 10

        # Check if save_item meets the criteria
        if not meets_criteria(content_item):
            return  # If it doesn't meet the criteria, exit the function and do not save to CSV
            
        await self.save_data_to_csv(save_item=content_item, store_type="contents")

    async def store_comment(self, comment_item: Dict):
        """
        Xiaohongshu comment CSV storage implementation
        Args:
            comment_item: comment item dict

        Returns:

        """
        await self.save_data_to_csv(save_item=comment_item, store_type="comments")


class XhsDbStoreImplement(AbstractStore):
    async def store_content(self, content_item: Dict):
        """
        Xiaohongshu content DB storage implementation
        Args:
            content_item: content item dict

        Returns:

        """
        from .xhs_store_db_types import XHSNote
        note_id = content_item.get("note_id")
        if not await XHSNote.filter(note_id=note_id).first():
            content_item["add_ts"] = utils.get_current_timestamp()
            note_pydantic = pydantic_model_creator(XHSNote, name="XHSPydanticCreate", exclude=('id',))
            note_data = note_pydantic(**content_item)
            note_pydantic.model_validate(note_data)
            await XHSNote.create(**note_data.model_dump())
        else:
            note_pydantic = pydantic_model_creator(XHSNote, name="XHSPydanticUpdate", exclude=('id', 'add_ts'))
            note_data = note_pydantic(**content_item)
            note_pydantic.model_validate(note_data)
            await XHSNote.filter(note_id=note_id).update(**note_data.model_dump())

    async def store_comment(self, comment_item: Dict):
        """
        Xiaohongshu content DB storage implementation
        Args:
            comment_item: comment item dict

        Returns:

        """
        from .xhs_store_db_types import XHSNoteComment
        comment_id = comment_item.get("comment_id")
        if not await XHSNoteComment.filter(comment_id=comment_id).first():
            comment_item["add_ts"] = utils.get_current_timestamp()
            comment_pydantic = pydantic_model_creator(XHSNoteComment, name="CommentPydanticCreate", exclude=('id',))
            comment_data = comment_pydantic(**comment_item)
            comment_pydantic.model_validate(comment_data)
            await XHSNoteComment.create(**comment_data.model_dump())
        else:
            comment_pydantic = pydantic_model_creator(XHSNoteComment, name="CommentPydanticUpdate",
                                                      exclude=('id', 'add_ts',))
            comment_data = comment_pydantic(**comment_item)
            comment_pydantic.model_validate(comment_data)
            await XHSNoteComment.filter(comment_id=comment_id).update(**comment_data.model_dump())


class XhsJsonStoreImplement(AbstractStore):
    json_store_path: str = "data/xhs"
    lock = asyncio.Lock()

    def make_save_file_name(self, store_type: str) -> str:
        """
        make save file name by store type
        Args:
            store_type: Save type contains content and comments（contents | comments）

        Returns:

        """
        return f"{self.json_store_path}/{crawler_type_var.get()}_{store_type}_{utils.get_current_date()}.json"

    async def save_data_to_json(self, save_item: Dict, store_type: str):
        """
        Below is a simple way to save it in json format.
        Args:
            save_item: save content dict info
            store_type: Save type contains content and comments（contents | comments）

        Returns:

        """
        pathlib.Path(self.json_store_path).mkdir(parents=True, exist_ok=True)
        save_file_name = self.make_save_file_name(store_type=store_type)
        save_data = []

        async with self.lock:
            if os.path.exists(save_file_name):
                async with aiofiles.open(save_file_name, 'r', encoding='utf-8') as file:
                    save_data = json.loads(await file.read())

            save_data.append(save_item)
            async with aiofiles.open(save_file_name, 'w', encoding='utf-8') as file:
                await file.write(json.dumps(save_data, ensure_ascii=False))

    async def store_content(self, content_item: Dict):
        """
        content JSON storage implementation
        Args:
            content_item:

        Returns:

        """
        def meets_criteria(item):
            # Example criteria: Check if 'liked_count' is greater than 20 and comment_count is greater than 10
            return int(item.get('liked_count', 0)) > 20 and int(item.get('comment_count', 0)) > 10

        # Check if save_item meets the criteria
        if not meets_criteria(content_item):
            return  # If it doesn't meet the criteria, exit the function and do not save to CSV
        await self.save_data_to_json(content_item, "contents")

    async def store_comment(self, comment_item: Dict):
        """
        comment JSON storage implementatio
        Args:
            comment_item:

        Returns:

        """
        await self.save_data_to_json(comment_item, "comments")
