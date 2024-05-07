const sql = require('mssql')

const config = {
    user:'sa',
    password:'Prueba123',
    server:'localhost',
    database:'BD_API_SISTEMAS_EMBEBIDOS',
    options: {
        encrypt: false, // for azure
        trustServerCertificate: true // change to true for local dev / self-signed certs
      }
}

const getConnection = async function (){
    try{
        const conexion = await sql.connect(config) //conexion es el objeto que representa la conexion logica con la base de datos
        return conexion
    }
    catch(error){
        console.log(error)
    }    
}

module.exports = {
    getConnection
}
