<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Merge HTML to PDF - README</title>
  <style>
    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background: #f9fafb;
      color: #333;
      margin: 0;
      padding: 40px 20px;
      line-height: 1.7;
    }
    .container {
      max-width: 800px;
      margin: auto;
      background: #fff;
      padding: 40px;
      border-radius: 12px;
      box-shadow: 0 8px 25px rgba(0,0,0,0.1);
    }
    h1, h2, h3 {
      color: #2c3e50;
    }
    code {
      background-color: #f1f1f1;
      padding: 3px 6px;
      border-radius: 4px;
      font-size: 0.95em;
    }
    pre {
      background-color: #f1f1f1;
      padding: 12px;
      border-radius: 6px;
      overflow-x: auto;
    }
    a {
      color: #2980b9;
      text-decoration: none;
    }
    a:hover {
      text-decoration: underline;
    }
    .screenshot {
      margin: 30px 0;
      text-align: center;
    }
    footer {
      text-align: center;
      font-size: 0.9em;
      color: #888;
      margin-top: 40px;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>📄 Merge Multiple HTML Files to Single PDF</h1>
    <p>
      This project is a browser-based tool that allows you to select up to 45 HTML files and merge them into a single downloadable PDF file. No backend or server required – everything runs directly in your browser.
    </p>

    <h2>🚀 Features</h2>
    <ul>
      <li>✔️ Upload and merge up to 45 HTML files</li>
      <li>✔️ Choose between <strong>Portrait</strong> and <strong>Landscape</strong> orientation</li>
      <li>✔️ Handles images, styles, and large content with pagination</li>
      <li>✔️ Clean, user-friendly interface</li>
      <li>✔️ Pure frontend – no installation needed</li>
    </ul>

    <h2>📸 Screenshot</h2>
    <div class="screenshot">
      <img src="https://via.placeholder.com/750x400?text=App+Screenshot" alt="App Screenshot" width="100%" />
    </div>

    <h2>📦 Technologies Used</h2>
    <ul>
      <li><strong>HTML5</strong> – App structure</li>
      <li><strong>CSS3</strong> – Styling and layout</li>
      <li><strong>JavaScript</strong> – App logic</li>
      <li><a href="https://github.com/parallax/jsPDF" target="_blank">jsPDF</a> – PDF generation</li>
      <li><a href="https://html2canvas.hertzen.com/" target="_blank">html2canvas</a> – Render HTML as images</li>
      <li><a href="https://pdf-lib.js.org/" target="_blank">PDF-lib</a> – Merge multiple PDFs</li>
    </ul>

    <h2>📁 File Structure</h2>
    <pre>
📁 merge-html-to-pdf
├── index.html         ← Main app
├── README.html        ← This file
└── assets/            ← Screenshots or icons (optional)
    </pre>

    <h2>🛠️ How to Use</h2>
    <ol>
      <li>Clone or download the repository.</li>
      <li>Open <code>index.html</code> in your browser.</li>
      <li>Select multiple <code>.html</code> files using the file input.</li>
      <li>Choose your desired orientation.</li>
      <li>Click <strong>"Convert & Download Merged PDF"</strong>.</li>
    </ol>

    <h2>👨‍💻 Author</h2>
    <p>
      <strong>Harsh Verma</strong><br>
      Certified Android & MERN Developer<br>
      🌐 <a href="https://harshnexus.com" target="_blank">harshnexus.com</a> (if available)<br>
      📧 <a href="mailto:your-email@example.com">your-email@example.com</a>
    </p>

    <h2>📃 License</h2>
    <p>
      This project is open-source and available under the <a href="https://opensource.org/licenses/MIT" target="_blank">MIT License</a>.
    </p>

    <footer>
      Made with 💙 by Harsh Verma – 2025
    </footer>
  </div>
</body>
</html>
