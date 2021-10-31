import express from 'express';
const app = express()
const port = 3001

import cors from "cors";

//app.use(bodyParser.urlencoded({ extended: true }))
app.use(express.json())
app.use(cors())

let inputbuffer: any[] = []
let colorwheel: any[] = []

app.get('/', (req, res) => {

      res.jsonp({
            "get" : inputbuffer
      })

      if(inputbuffer.length > 0)
            inputbuffer = [];
      

});

app.post('/', (req, res) => {

      if(inputbuffer.length > 10)
            inputbuffer.shift()
      
      inputbuffer.push(req.body)

      res.jsonp({
            colorwheel
      })
});

app.post('/colors', (req, res) => {
      colorwheel = req.body.colorwheel;

      res.jsonp({
            "post" : "SUCCESS"
      })
});

app.get('/colors', (req, res) => {
      res.jsonp({
            "post" : colorwheel
      })
});

app.listen(port , () => {
      console.log("Listening on Port ", port);
})