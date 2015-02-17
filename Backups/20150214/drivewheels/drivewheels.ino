/*
 Serial1 : Dynamixel_Poart
 Serial2 : Serial_Poart(4pin_Molex)
 Serial3 : Serial_Poart(pin26:Tx3, pin27:Rx3)
 
 TxD3(Cm9_Pin26) <--(Connect)--> RxD(PC)
 RxD3(Cm9_Pin27) <--(Connect)--> TxD(PC)
 */
byte index = 0;
int input;

void setup(){
  //Serial3 Serial initialize
  Serial3.begin(9600); 
}

void loop(){
  // when you typed any character in terminal
  if(Serial3.available() > 0){
    
    SerialUSB.println("X"); //return message to computer for timing
    
    //consume all data on serial port and load inData array
    int inData[20];
    while(Serial3.available() > 0){
      if(index < 19){
        innput = Serial3.read();
        inData[index] = inChar;
        index++;
        inData[index] = '\0';
      }
    }
  }
}

