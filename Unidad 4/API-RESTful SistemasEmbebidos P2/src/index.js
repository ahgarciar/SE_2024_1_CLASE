const express = require('express') // importacion de modulo para crear la api
const v1 = require('./v1/routes/Routes')

const app = express();
const PORT = process.env.PORT || 3000;
app.use(express.json()) //json parser --//habilita a la api para trabajar con json


//ACCESO A LA API ....
// http://localhost:3000    127.0.0.1
// http://ip local / publica / homologada / privada
// http://DNS


//vincula las rutas ("NOMBRE" QUE SE USARA PARA LLAMAR MEDIANTE HTTP A LAS FUNCIONES DE LA API)
app.use("/api/v1", v1)

///////////////Informacion que se despliega al acceder a http://localhost:3000/ ...
app.get("/",(req,res)=>{
    res.send(`<h1>API RESTful en NodeJS</h1>`)
})
//////////////////
///////////////Informacion que se despliega al acceder a http://localhost:3000/api ...
app.get("/api",(req,res)=>{
    res.send(`<h1>INFO DE LA API</h1>`)
})
//////////////////

//inicia la api y ejecuta una funcion callback que retroalimenta el estado en la consola/terminal
const servidor = app.listen(PORT, function(){ //()=>{  //funcion flecha
    console.log(`Servidor escuchando en el Puerto: ${PORT}`);
})

//servidor.setMaxListeners(10);