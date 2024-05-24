const express = require("express")
const mongoose = require("mongoose")

const app = express()

// Proxy requests to the Flask backend
app.use('/api', createProxyMiddleware({ target: 'http://localhost:5000', changeOrigin: true }));

// Serve frontend files
app.use(express.static(path.join(__dirname, 'frontend', 'build')));

// Catch-all route to serve frontend's index.html
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'frontend', 'build', 'index.html'));
});

// mongoose.connect('', {
//     useNewUrlParser: true,
//     useUnifiedTopology: true,
// })

const port = process.env.PORT || 3000;

app.listen(port, () => {
    console.log('Server is running on port 3000')
})