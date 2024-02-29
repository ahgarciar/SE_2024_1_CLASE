int leds[3] = {11, 12, 13};

bool leds_estado[3] = {false, false, false }; //estado de los leds

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(100); //ms
  
  for(int i = 0; i<3; i++){
    pinMode(leds[i], OUTPUT);
  }

}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){
    int v= Serial.readString().toInt(); //indice del foco a alterar

    //alteramos el estado del foco 
    leds_estado[v] != leds_estado[v];   //si esta apagado, pasa a prendido y viceversa

    digitalWrite(leds[v], leds_estado[v]);  //aplica el nuevo estado

  }
  delay(100);

}
