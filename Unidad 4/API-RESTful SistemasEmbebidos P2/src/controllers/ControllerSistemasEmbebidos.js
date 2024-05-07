
const services = require('../services/ServiceSistemasEmbebidos')

/////////////////////////////////////////////////////////////////////////////////////////////////////////

const getAll_Historico_Dispositivos = async function(req,res){

    const resultado = await services.getAll_Historico_Dispositivos()    
    //console.log(resultado)
    res.status(201).send(resultado) //Envia el resultado a traves de la API

}

/////////////////////////////////////////////////////////////////////////////////////////////////////////

const getDispositivo_Historico = async function(req,res){ 
    const {params:{idDispositivo}} = req 
    //console.log(typeof idSensor)
    if (!isNaN(idDispositivo)){
        const resultado = await services.getDispositivo_Historico(idDispositivo)
        res.status(200).send(resultado) //Envia el resultado a traves de la API
    }
    else{
        res.status(501).send("El valor ingresado no es valido") //Envia el resultado a traves de la API
    }
}

/////////////////////////////////////////////////////////////////////////////////////////////////////////

const getLastDispositivoHistorico = async function(req,res){    
    const {params:{idDispositivo}} = req 
    //console.log(typeof idSensor)
    if (!isNaN(idDispositivo)){
        const resultado = await services.getLastDispositivoHistorico(idDispositivo)
        //res.status(200).send(resultado) //Envia el resultado a traves de la API

        v = resultado["valor"]
        console.log(v)

        res
        .setHeader('content-type', "application/json")
        .status(201).send("{\"Valor\":"+ parseInt(v) + "}")        

    }
    else{
        res.status(501).send("El valor ingresado no es valido") //Envia el resultado a traves de la API
    }
}

/////////////////////////////////////////////////////////////////////////////////////////////////////////

//Ejemplo de body para INSERT, DELETE y UPDATE ->
/*
{
    "Id_Dispositivo": 1,
    "Id_Historico": 1,
    "Valor":155
}


o Estructura para multiples objetos...

{"objetos":[
            {
            "Id_Dispositivo": "3",
            "Id_Historico": 1,
            "Valor":155
        }
    ]
}

*/

/////////////////////////////////////////////////////////////////////////////////////////////////////////

const insertHistorico = async function(req,res){
    const { body } = req; //recepcion del objeto que sera creado/insertado

    console.log(body)
    //console.log("rev: ", body["objetos"])

    for(const obj of body["objetos"]) {
        // *** OBJETO QUE CONTIENE LA INFORMACION DE LA NUEVA REVIION ***
            // COMPRUEBA QUE TODOS LOS CAMPOS DE CADA OBJETO TENGAN VALORES
            
            if (
                (obj.Id_Dispositivo !== undefined && obj.Id_Dispositivo !== null && obj.Id_Dispositivo !== '') &&                
                (obj.Valor !== undefined && obj.Valor !== null && obj.Valor !== '')
            ){
                //console.log("Objeto Completo")
                console.log("obj: ", obj)


                const newObj = {
                    Id_Dispositivo: obj.Id_Dispositivo,
                    Id_Historico: obj.Id_Historico,
                    Valor: obj.Valor,                    
                };
                            
                resultado = await services.insertHistorico(newObj)    
                console.log("Registro Guardado")

                //resultado =  "{\"Resultado\": \"Inserción Correcta\"}"
          
            } 
            else{        
                res.status(400)
                .send({
                    status:"Error", data:{
                        error:"Faltan datos"}
                    })
                return //Termina toda ejecucion
            }
} //FIN CICLO FOR

//SE EJECUTA SI TERMINA EL CICLO FOR 
res
    .setHeader('content-type', "application/json") //'text/plain')
    .status(201)
    .send(resultado)

}

/////////////////////////////////////////////////////////////////////////////////////////////////////////

const updateHistorico = async function(req,res){
    const {params:{idHistorico}} = req 
    //console.log(typeof idSensor)
    if (isNaN(idHistorico)){
        res
            .setHeader('content-type', "application/json") //'text/plain')
            .status(501)
            .send("El valor ingresado no es valido")
        return 
    }
    
    const { body } = req; //recepcion del objeto que sera creado/insertado

    console.log(body)
    //console.log("rev: ", body["objetos"])
    
    for(const obj of body["objetos"]) {
        // *** OBJETO QUE CONTIENE LA INFORMACION DE LA NUEVA REVIION ***
            // COMPRUEBA QUE TODOS LOS CAMPOS DE CADA OBJETO TENGAN VALORES
            
            if (
                (obj.Id_Dispositivo !== undefined && obj.Id_Dispositivo !== null && obj.Id_Dispositivo !== '') &&
                (obj.Id_Historico !== undefined && obj.Id_Historico !== null && obj.Id_Historico !== '') &&
                (obj.Valor !== undefined && obj.Valor !== null && obj.Valor !== '')
            ){
                //console.log("Objeto Completo")
                console.log("obj: ", obj)


                const newObj = {
                    Id_Dispositivo: obj.Id_Dispositivo,
                    Id_Historico: obj.Id_Historico,
                    Valor: obj.Valor,                    
                };
                            
                resultado = await services.updateHistorico(idHistorico,newObj)    
                console.log("Registro Actualizado")

                //resultado =  "{\"Resultado\": \"Actualizacion Correcta\"}"
          
            } 
            else{        
                res.status(400)
                .send({
                    status:"Error", data:{
                        error:"Faltan datos"}
                    })
                return //Termina toda ejecucion
            }
} //FIN CICLO FOR

//SE EJECUTA SI TERMINA EL CICLO FOR 
res
    .setHeader('content-type', "application/json") //'text/plain')
    .status(201)
    .send(resultado)


}

/////////////////////////////////////////////////////////////////////////////////////////////////////////

const deleteHistorico = async function(req,res){
    
    const { body } = req; //objeto a ser creado

    console.log("body: ",  body)

    // COMPRUEBA QUE TODOS LOS CAMPOS TENGA VALORES
    Id_Historico =  body["objetos"][0].Id_Historico         

    if (
        Id_Historico == undefined || Id_Historico == null || Id_Historico == '' || isNaN(Id_Historico)
    ) {        
        res.status(400)
           .send({
            status:"Error", data:{
                error:"Faltan datos"}
            })
        return 
    }
    
    // *** OBJETO QUE CONTIENE LA INFORMACION DEL REGISTRO A ELIMINAR ***
    const ObjToDelete = {        
        Id_Historico: body["objetos"][0].Id_Historico
    };

    const resultado = await services.deleteHistorico(ObjToDelete)
    
    //resultado =  "{\"Resultado\": \"Registro Eliminado\"}"
    
    res
    .setHeader('content-type', "application/json") //'text/plain')
    .status(201)
    .send(resultado)


}


module.exports = {
    getAll_Historico_Dispositivos,
    getDispositivo_Historico,    
    getLastDispositivoHistorico,

    insertHistorico,
    updateHistorico,
    deleteHistorico

}

