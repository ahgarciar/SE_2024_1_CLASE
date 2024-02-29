int sensores[] = {A0, A1, A2};  //sensor1, sensor2, sensor3

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}
int i;
int res[] = {0,0,0};
int totLecturas = 10;

void loop() {
  // put your main code here, to run repeatedly:
  for(int idx_sensor = 0; idx_sensor<3; idx_sensor++){
    res[idx_sensor] = 0;
    ////////////////////////////////////
    for(int i=0; i<totLecturas;i++){
      res[idx_sensor] += analogRead(sensores[idx_sensor]);
      delayMicroseconds(10);
    }  
    res[idx_sensor] /= totLecturas;
    ////////////////////////////////////
  }
  ////////////////////////////////////
  Serial.println(String(res[0]) + " " + String(res[1]) + " " + String(res[2]));
  delay(100);
}
