// demo of Grove - Starter V2.0
// Loovee  2013-3-10
// this demo will show you how to use Grove - Button to control a LED
// when the button was pressed, the led will on 
// otherwise led off
// Grove - Button connect to D3
// Grove - LED connect to D7

const int pinButton = 3;                        // pin of button define here
const int pinLed    = 7;                        // pin of led define here
int incomingByte;

void setup()
{
    pinMode(pinButton, INPUT);                  // set button INPUT
    pinMode(pinLed, OUTPUT);                    // set led OUTPUT
    Serial.begin(9600);
}

void loop()
{
    Serial.println(digitalRead(pinButton));
    if(digitalRead(pinButton))                     // when button is pressed
    {
        digitalWrite(pinLed, HIGH);             // led on
    }
    else
    {
        if (Serial.available() > 0) {
        // read the oldest byte in the serial buffer:
          incomingByte = Serial.read();
        // if it's a capital H (ASCII 72), turn on the LED:
        if (incomingByte == 'H') {
          digitalWrite(pinLed, HIGH);
        } 
        // if it's an L (ASCII 76) turn off the LED:
        if (incomingByte == 'L') {
          digitalWrite(pinLed, LOW);
        }
      }  
    }
    
    delay(10);
}
