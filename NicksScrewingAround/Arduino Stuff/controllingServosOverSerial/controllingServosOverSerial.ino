
#define PWM1_PIN 9
#define PWM2_PIN 7


char pwm1 = 0;
char pwm2 = 0;
bool updatePwm1 = false;
bool updatePwm2 = false;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  getSerial();
}

#define BUF_SIZE 32
char rx_byte[BUF_SIZE] = {0, 0, 0, 0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0, 0, 0, 0};
char n = 0;

void getSerial(){
  if (Serial.available() > 0) {    // is a character available?
    rx_byte[n] = Serial.read();       // get the character
  
    // check if a number was received
    if ((rx_byte[n] >= '0') && (rx_byte[n] <= '9')) {
      Serial.print("Number received: ");
      Serial.println(rx_byte[n]);
    }
    else {
      Serial.println("Not a number.");
    }

    

    offset = 0;
    if(n == 2){
      pwm1 = 100*asciiNumToNum(rx_byte[0]) + 10*asciiNumToNum(rx_byte[1]) + asciiNumToNum(rx_byte[2]);
      Serial.print("pwm1: ");
      Serial.println(pwm1); 
      updatePwm1 = true;
    }

    if(n == 5){
      pwm2 = 100*asciiNumToNum(rx_byte[3]) + 10*asciiNumToNum(rx_byte[4]) + asciiNumToNum(rx_byte[5]);
      Serial.print("pwm2: ");
      Serial.println(pwm2);
      updatePwm2 = true;
    }
    n++;
    if(n >= BUF_SIZE){
      n = 0;
    }

  }  
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

void updatePwm(){
  if(updatePwm1 == true){
    analogWrite(PWM1_PIN, pwm1);
    updatePwm1 = false;
  }
  if(updatePwm2 == true){
    analogWrite(PWM2_PIN, pwm2);
    updatePwm2 = false;
  }
}



