int leds[3] = {11, 12, 13};

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
    int v= Serial.readString().toInt(); //indice del foco a prender

    for(int i = 0; i< 3; i++){
      digitalWrite(leds[i], 0);
    }

    digitalWrite(leds[v], leds_estado[v]);  //prende el led

  }
  delay(100);

}
