#define SHOLDER_PIN 9
#define ELBOW_PIN 8
#define HEIGHT_PIN 7

#define SHOLDER_FB_PIN A3
#define ELBOW_FB_PIN A2

#define KILL_PIN 3

#define PEN_UP_PWM 15
#define PEN_DOWN_PWM 0

char pwmSholder = 0;
char pwmElbow = 0;

char serialBuffer[256];
char bufferIdx = 0;
char penState = 'u';

char parseIdx = 0;

void setup(){
    pinMode(SHOLDER_FB_PIN, INPUT);
    pinMode(ELBOW_FB_PIN, INPUT);

    pinMode(KILL_PIN, INPUT_PULLUP);


    Serial.begin(9600);

}


void loop(){
    while(Serial.available()){
        serialBuffer[bufferIdx++] = Serial.read();
    }
    char offset = 1;
    if (serialBuffer[bufferIdx - offset] == '\0'){ //This should run
        offset = 14;
        if (serialBuffer[bufferIdx - offset] == 't' && serialBuffer[bufferIdx - offset + 1] == '1'){
            pwmSholder = serialBuffer[bufferIdx - offset + 3];
        } else {
            Serial.println('Sholder Pwm not found');
        }
        offset = 9;
        if (serialBuffer[bufferIdx - offset] == 't' && serialBuffer[bufferIdx - offset + 1] == '2'){
            pwmElbow = serialBuffer[bufferIdx - offset + 3];
        } else {
            Serial.println('Elbow Pwm not found');
        }
        offset = -4;
        if (serialBuffer[bufferIdx - offset] == 'p'){
            penState = serialBuffer[bufferIdx - offset + 2];
        } else {
            Serial.println('Pen State not found');
        }
    } else {
        Serial.println("There's an error, serial string not formatted correctly");
    }
    if (digitalRead(KILL_PIN) == LOW){
        pinMode(SHOLDER_PIN, OUTPUT);
        pinMode(ELBOW_PIN, OUTPUT);
        pinMode(HEIGHT_PIN, OUTPUT);

        analogWrite(SHOLDER_PIN, pwmSholder);
        analogWrite(ELBOW_PIN, pwmElbow);
        if (penState == 'u'){
            analogWrite(HEIGHT_PIN, PEN_UP_PWM);
        } else if (penState == 'd'){
            analogWrite(HEIGHT_PIN, PEN_DOWN_PWM);
        }
        
    }
    Serial.print("t1=");
    Serial.print(analogRead(SHOLDER_FB_PIN));
    Serial.print(",");
    Serial.print("t2=");
    Serial.print(analogRead(ELBOW_FB_PIN));
    Serial.print(",/n");




}