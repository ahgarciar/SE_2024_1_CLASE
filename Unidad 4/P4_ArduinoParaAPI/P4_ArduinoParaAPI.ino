int actuadores[3] = {9, 10, 11};  //Simulados por LEDS 
int sensores[3] = {A0, A1, A2};  //Simulados por Potenciometros
int index; 

void setup() { 
  Serial.begin (9600);  //INICIA COMUNICACION SERIAL
  Serial.setTimeout(10); //DEFINE EL TIMEOUT

  for(index = 0; index<3; index++){
    pinMode(actuadores[index], OUTPUT);     
  }  
}
 

float Read_and_Mean(int index_sensor){
  float prom = 0;
  for(int i = 0; i<10; i++){
    prom += analogRead(sensores[index_sensor]);
    delayMicroseconds(10); //se realiza una lectura cada 10 microsegundos
  }
  prom /= 30; 
  return prom;
}

String valores_sensores;
String cadena;
int valor;
void loop() {   
  //LECTURA DE DATOS DE LOS SENSORES
  valores_sensores = "";
  for(index = 0; index<3; index++){
    valores_sensores = valores_sensores + "-" + String(Read_and_Mean(index));
  }

  //ENVIO DE LOS DATOS DE LOS SENSORES A PYTHON
  Serial.println("A" + valores_sensores + "Z");

  //RESPUESTA DE PYTHON
  if(Serial.available()>0){
    cadena = Serial.readString();
    char *cadena_aux = cadena.c_str();  //convierte a la cadena original en un apuntador
    char *token = strtok(cadena_aux, "-"); //obtiene un token que va desde la primera posición de la cadena hasta la primera aparicion de "-" 
        
    index = 0;
    while(token != NULL){
      Serial.println(token);       //solo para pruebas... comentar en la version de "produccion"
      valor = String(token).toInt();
      digitalWrite(actuadores[index], valor);          
      index++;
      token = strtok(NULL, "-"); 
    }
  } 
  
  delay(100); 
}
