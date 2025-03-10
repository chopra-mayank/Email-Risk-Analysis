const express = require('express');
const mongoose = require('mongoose');
const routes = require('./routes');
const morgan = require('morgan');

const app = express();
const PORT = 3000;

app.use(express.json());
app.use(morgan('dev'));
mongoose.connect('mongodb://localhost:27017/emailDB', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
})
.then(() => console.log("MongoDB connected successfully"))
.catch(err => console.error("MongoDB connection error:", err));

app.use('/', routes);

app.listen(PORT, () => {
  console.log(`Node.js server running on http://localhost:${PORT}`);
});