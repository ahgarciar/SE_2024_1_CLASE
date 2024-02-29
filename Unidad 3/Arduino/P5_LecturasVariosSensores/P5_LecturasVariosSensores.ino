int sensor1 = A0;
int sensor2 = A1;
int sensor3 = A2;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}
int i;
int res1, res2, res3;
int totLecturas = 10;
void loop() {
  // put your main code here, to run repeatedly:
  res1 = 0;
  res2 = 0;
  res3 = 0;
  ////////////////////////////////////
  for(int i=0; i<totLecturas;i++){
    res1 += analogRead(sensor1);
    delayMicroseconds(10);
  }  
  res1 /= totLecturas;
  ////////////////////////////////////
  for(int i=0; i<totLecturas;i++){
    res2 += analogRead(sensor2);
    delayMicroseconds(10);
  }  
  res2 /= totLecturas;
  ////////////////////////////////////
  for(int i=0; i<totLecturas;i++){
    res3 += analogRead(sensor3);
    delayMicroseconds(10);
  }  
  res3 /= totLecturas;
  ////////////////////////////////////
  Serial.println(String(res1) + " " + String(res2) + " " + String(res3));
  delay(100);
}
