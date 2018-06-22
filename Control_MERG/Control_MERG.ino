#include <Servo.h>

Servo myservo;
int pos = 0;  
char data;
char data;

void setup() {
  
  Serial.begin(9600);
  myservo.attach(PB3);
  Serial.begin(9600);
  DDRA  = 0b11111100;     
  DDRC  = 0b11111100;     
  DDRD = 0b11110000;
  PORTD = 0b11111111;
}

void loop() {
  
  if (Serial.available()> 0)
  {
    data = Serial.read();
  }
    //Forward
   if (data == '0')
    {
      PORTC = 0b01010000;
      PORTA = 0b01010000;
    }

   //Backward
   else if (data == '1')
    {
      PORTC = 0b10100000;
      PORTA = 0b10100000; 
    }

    //Right
   else if (data == '2')
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
    
     //EXIT
    else if (data == '7')
    {
       PORTC = 0b00000000;
       PORTA = 0b00000000;
    }
    
    //Give Food
     else if (data == '4')
    {
      for (pos = 0; pos <= 90; pos += 1)  
  {
    myservo.write(pos);             
    delay(15);                      
  }
    }

    //Close Flap
     else if (data == '5')
    {
      for (pos = 90; pos >= 0; pos -= 1)  
  {
    myservo.write(pos);             
    delay(15);                      
  }
    }    
}
