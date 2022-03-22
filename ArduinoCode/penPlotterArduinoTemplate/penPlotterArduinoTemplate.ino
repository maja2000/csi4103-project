//Different states and tasks of the Arduino
//NOTE: states CONVERT_XY_THETA and CONVERT_THETA_PWM will be done on Pi instead

enum PlotterState {
  IDLE,
  FETCHING_INSTRUCTIONS,
  SENDING_DATA,
  DRAWING,
  WAITING_TO_DRAW,
  CONVERT_XY_THETA,
  CONVERT_THETA_PWM,
  INTERPOLATE_XY_POINTS,
  EMERGENCY_STOP
};

PlotterState plotterState = IDLE;

//test values
float xList[] = {1,3,5};
float yList[] = {2,4,6};

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  switch(plotterState){
    /////////////////////////////////////////////////////////
    //State when arduino is waiting for something to do
    /////////////////////////////////////////////////////////
    case IDLE:

      break;

    /////////////////////////////////////////////////////////
    //State when arduino grabs array of points (x,y) to draw
    //arduino needs to get length of array, then the points (x1, x2, ... , xn) then (y1, y2, ... , yn)
    //NOTE: this will be changed to grab an array of (pwm1, pwm2) points instead
    /////////////////////////////////////////////////////////
    case FETCHING_INSTRUCTIONS:
      if (Serial.available() > 0){

        //First value that Pi sends should be the length of the coordinate list
        int length_list = Serial.read();
        Serial.print("You sent me: ");
        Serial.println((String)length_list);

        //Creating an X list and Y list
        int xList[length_list];
        int yList[length_list];

        //Pi sends X coordinate, then Y coordinate
        //This repeats until Pi sends all of the pairs of coordinates
        for(int i=0; i<length_list; i++){
          //add X coordinate to the X list
          int coordX = Serial.read();
          xList[i] = coordX;
          Serial.print("You sent me X: ");
          Serial.println((String)xList[i]);

          //add Y coordinate to the Y list
          int coordY = Serial.read();
          yList[i] = coordY;
          Serial.print("You sent me Y: ");
          Serial.println((String)yList[i]);
        }
      }
      delay(1000);
      break;

    /////////////////////////////////////////////////////////
    //State when arduino sends data back to pi
    //To send: pot values, status, ...
    /////////////////////////////////////////////////////////
    case SENDING_DATA:
      //if(Serial.available() > 0)
      //Serial.print()
      break;

    /////////////////////////////////////////////////////////
    //State when arduino draws
    //loops through points (pwm1, pwm2), and sends them to pins
    /////////////////////////////////////////////////////////
    case DRAWING:
      //use analogWrite() to send the pwm points to pins

      break;

    /////////////////////////////////////////////////////////
    //State where arduino is waiting for go ahead (from push btn on gpio)
    /////////////////////////////////////////////////////////
    case WAITING_TO_DRAW:

      break;

    /////////////////////////////////////////////////////////
    //State where array of points (x,y) is converted to array of angles (theta1, theta2) where theta is the angle of the arm
    //NOTE: this conversion will be done on the Pi instead
    /////////////////////////////////////////////////////////
    case CONVERT_XY_THETA:
      //
      break;

    /////////////////////////////////////////////////////////
    //State where array of angles (theta1, theta2) is converted into pwm values to write to pins
    //NOTE: this conversion will be sone on the Pi instead
    /////////////////////////////////////////////////////////
    case CONVERT_THETA_PWM:
      //degrees 0 to 180
      //pwm 0 to 255

      //pwm = (theta1 / 180)*255
      
      break;

    /////////////////////////////////////////////////////////
    //State where array of points (x,y) is expanded so that each pair of points (xn, yn) and (xn+1, yn+1) are connected by a line of points
    //This increases the resolution of the pen plotter and ensures that points are connected together by straight lines
    //NOTE: this logic is presented as the Arduino recieves an array of coordinates. This logic is to be changed.
    /////////////////////////////////////////////////////////
    case INTERPOLATE_XY_POINTS:
      // take the difference of the 2 points, find the X-difference and Y-difference. Divide each by the desired amount. Rise and run.
      int divider = 3; //amount of points wanted between (xn, yn) and (xn+1, yn+1). this is a set value.
      int len_existing_list = 3; //value that Pi sent before in FETCHING_INSTRUCTIONS
      int new_list_size = len_existing_list + (divider * (len_existing_list-1)); //size of expanded list
      
      //initializing a new set 
      float newXList[new_list_size];
      float newYList[new_list_size];

      //setting the value for the first element in each list
      newXList[0] = xList[0];
      newYList[0] = yList[0];

      //for the length of each list, we want to take 2 elements at a time
      //we find the difference between the 2 value,
      //then find the incremental value needed to add more points inbetween
//      for(int i=0; i<len_existing_list-1; i++){
//        float firstX = xList[i];
//        float secondX = xList[i+1];
//        float differenceX = secondX - firstX;
//        float incX = differenceX / divider;
//
//        float firstY = yList[i];
//        float secondY = yList[i+1];
//        float differenceY = secondY - firstY;
//        float incY = differenceY / divider;
//        
//        for(int j=1; j < (divider+1); j++){
//          newXList[j] = newXList[j-1] + incX;
//          newYList[j] = newYList[j-1] + incY;
//        }       
//      }
     
      break;

    /////////////////////////////////////////////////////////
    //State where if shit goes wrong, plotter is stopped and can be recovered from
    /////////////////////////////////////////////////////////
    case EMERGENCY_STOP:

      break;
  }

}
