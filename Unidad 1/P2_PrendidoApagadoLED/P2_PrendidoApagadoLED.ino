//Prendido de un LED
//LED digital*** --- analogico

int led = 13; //pin -- pin digital

void setup() {
  // put your setup code here, to run once:
  //CONFIGURACION DEL MODO DE TRABAJO DEL PIN ASOCIADO A LA VARIABLE "LED"
  pinMode(led, OUTPUT);  // OUTPUT   INPUT 
}

//OSCILADOR DE CRISTAL DE 16MHz
void loop() {
  // put your main code here, to run repeatedly:

    //delay(1000); //milisegundo

    digitalWrite(led,1);
    delay(1000); //milisegundo
    digitalWrite(led,0);

    //delay(1000); //milisegundo

}
