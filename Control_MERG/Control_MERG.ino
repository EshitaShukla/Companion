/*
  LED Flick
  Welcome to robotics
  
  By Society of Robotics and Automation, VJTI
*/

/** Put your setup code here, to run once 
 *  setup() is called automatically once every time bot is reset or started.
 *  It is usually used to do all initialization.
 */

char data;

void setup() {          
  //Port Initialization - DDRX controls the input/output status of port X. 
  Serial.begin(9600);
  DDRA  = 0b11111100;     //C7 C6 C5 C4 C3 C2 are declared as output and C1 C0 are declared as input.
  DDRC  = 0b11111100;     //B0 B1 are declared as output and B7 B6 B5 B4 B3 B2 are declared as input.
  DDRD = 0b11110000;
  PORTD = 0b11111111;
}

/** Put your main code here which you want to run repeatedly
 *  loop() is function which is called again and again infinitely.
 *  It is called automatically after the setup() function finishes execution.
 */
void loop() {
  
  if (Serial.available()> 0)
  {
    data = Serial.read();
  }
    //Forward
   if (data == '1')
    {
      PORTC = 0b01010000;
      PORTA = 0b01010000;
    }

   //Backward
   else if (data == '0')
    {
      PORTC = 0b10100000;
      PORTA = 0b10100000; 
    }

    //Right
   else if (data == '4')
    {
      PORTC = 0b00010000;
      PORTA = 0b00010000;  
    }

    //Left
   else if (data == '3')
    {
      PORTC = 0b01000000;
      PORTA = 0b01000000; 
    }

    //quit
    else if (data == '5')
    {
       PORTC = 0b00000000;
       PORTA = 0b00000000;
    }
    
}
