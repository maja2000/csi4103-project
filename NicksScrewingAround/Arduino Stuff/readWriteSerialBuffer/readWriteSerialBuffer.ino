void setup() {
  Serial.begin(9600);
}

char rx_byte[3] = {0, 0, 0};
int theVal = 0;
char n = 0;

void loop() {
  if (Serial.available() > 0) {    // is a character available?
    rx_byte[n++] = Serial.read();       // get the character
  
    // check if a number was received
    if ((rx_byte >= '0') && (rx_byte <= '9')) {
      Serial.print("Number received: ");
      Serial.println(rx_byte);
    }
    else {
      Serial.println("Not a number.");
    }
    theVal = 100*asciiNumToNum(rx_byte[2]) + 10*asciiNumToNum(rx_byte[1]) + asciiNumToNum(rx_byte[0]);
    Serial.print("The number is: ");
    Serial.println(theVal);
    if(n >= 3){
      n = 0;
    }

  } // end: if (Serial.available() > 0)
}


char asciiNumToNum(char num){
  switch(num){
    case '0':
      return 0;
    case '1':
      return 1;
    case '2':
      return 2;
    case '3':
      return 3;
    case '4':
      return 4;
    case '5':
      return 5;
    case '6':
      return 6;
    case '7':
      return 7;
    case '8':
      return 8;
    case '9':
      return 9;
    default:
      return 0;
  }
}