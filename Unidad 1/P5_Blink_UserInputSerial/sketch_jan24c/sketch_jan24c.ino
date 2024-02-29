int led = 13;

void setup() {
  // put your setup code here, to run once:
  pinMode(led, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()>0){ //si hay info que leer en el buffer.. entonces...
    //considerando usuarios perfectos que solo enviaran "1" o "0"...
    int resultado = Serial.readString().toInt(); 

    if (resultado == 1){
      digitalWrite(led, 1);  //1 prender  0 = apagar  HIGH / LOW
      Serial.println("LED ENCEDIDO");
      //delay(1000);  //NO ES NECESARIO NI DESEABLE PONERLO AQUI
    }else{
      digitalWrite(led, 0);
      Serial.println("LED APAGADO");
      //delay(1000);  //NO ES NECESARIO NI DESEABLE PONERLO AQUI
    }
  }
  delay(10);
}
