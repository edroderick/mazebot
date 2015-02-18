/*
 Serial1 : Dynamixel_Poart
 Serial2 : Serial_Poart(4pin_Molex)
 Serial3 : Serial_Poart(pin26:Tx3, pin27:Rx3)
 
 TxD3(Cm9_Pin26) <--(Connect)--> RxD(PC)
 RxD3(Cm9_Pin27) <--(Connect)--> TxD(PC)
 */

#define DXL_BUS_SERIAL1 1 //Dynamixel on Serial1(USART1) <-OpenCM9.04 
#define DXL_BUS_SERIAL2 3 //Dynamixel on Serial2(USART2) <-LN101,BT210 
#define DXL_BUS_SERIAL3 3 //Dynamixel on Serial3(USART3) <-OpenCM 485EXP

Dynamixel Dxl(DXL_BUS_SERIAL1);

char inChar;
byte index = 0;
int maxspeed = 400;


void setup() {
  // Set up the pin 10 as an output:
  pinMode(BOARD_LED_PIN, OUTPUT);
  Serial3.begin(57600);
  Dxl.begin(3);
}


void loop() {
 

  if(Serial3.available() > 0){
    char inData[20];
    while(Serial3.available()>0){
      if(index < 19){
        inChar = Serial3.read(); //read a character
        inData[index] = inChar;
        index++;
        inData[index] = '\0';
      }
    }
  
  index = 0;
  SerialUSB.print("ret: ");
  SerialUSB.println(inData);
  
  if(inData[0] == char(68)){
    
    for(int i=0; i<100; i++){
      toggleLED();
      delay(100);
    }
  }
  delay(20);
}
}

/*

  if(motor1[1] == "0"){
    Dxl.wheelMode(motor1[0]);
    Dxl.goalSpeed(motor1[0], maxspeed*motor1[2]);
    digitalWrite(BOARD_LED_PIN, HIGH);   
  }
  if(motor2[1] == "0"){
    Dxl.wheelMode(motor2[0]);
    Dxl.goalSpeed(motor2[0], maxspeed*motor2[2]);
  }
  
  delay(100);
*/


