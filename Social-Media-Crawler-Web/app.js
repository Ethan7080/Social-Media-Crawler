const express = require('express');
const { exec } = require('child_process');
const fs = require('fs');
const app = express();
const port = 3000;

app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static('public'));

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/public/index.html');
});

app.post('/run-script', (req, res) => {
  const command = `cd MediaCrawler-main && source venv/bin/activate && python main.py --platform xhs --lt qrcode --type search`;

  exec(command, (error, stdout, stderr) => {
    if (error) {
      console.error(`Execution error: ${error}`);
      return res.status(500).json({ error: `Execution error: ${error.message}` });
    }


    // The output handling or response to the client should be here
    // (not shown in the original snippet you provided)
  });
});

// Download endpoint
app.get('/download', (req, res) => {
  const filePath = "MediaCrawler-main/data/xhs/ "; // File path to the file you want users to download
  res.download(filePath, 'output.txt', (err) => {
    if (err) {
      console.error("File download error:", err);
      if (!res.headersSent) {
        res.status(500).send("Error occurred during file download");
      }
    }
  });
});

app.listen(port, () => {
  console.log(`Server listening at http://localhost:${port}`);
});