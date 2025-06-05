const express = require("express");
const path = require("path");

const app = express();
const PORT = process.env.PORT || 3000;

// Роздаємо всі файли з папки public як статичні
app.use(express.static(path.join(__dirname, "public")));

// Якщо клієнт запитує будь-що, що не існує як файл, повертаємо index.html
app.get("*", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "index.html"));
});

app.listen(PORT, () => {
  console.log(`Frontend запущено на порті ${PORT}`);
});
