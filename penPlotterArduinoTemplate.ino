


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


void setup() {
  // put your setup code here, to run once:

}

void loop() {
  switch(plotterState){
    //State when arduino is waiting for something to do
    case IDLE:

      break;
    //State when arduino grabs array of points (x,y) to draw
    //arduino needs to get length of array, then the points (x1, x2, ... , xn) then (y1, y2, ... , yn)
    case FETCHING_INSTRUCTIONS:

      break;
    //State when arduino sends data back to pi
    //To send: pot values, status, ...
    case SENDING_DATA:

      break;
    //State when arduino draws
    //loops through points (pwm1, pwm2), and sends them to pins
    case DRAWING:

      break;
    //State where arduino is waiting for go ahead (from push btn on gpio)
    case WAITING_TO_DRAW:

      break;
    //State where array of points (x,y) is converted to array of angles (theta1, theta2) where theta is the angle of the arm
    case CONVERT_XY_THETA:

      break;
    //State where array of angles (theta1, theta2) is converted into pwm values to write to pins
    case CONVERT_THETA_PWM:

      break;
    //State where array of points (x,y) is expanded so that each pair of points (xn, yn) and (xn+1, yn+1) are connected by a line of points
    //This increases the resolution of the pen plotter and ensures that points are connected together by straight lines
    case INTERPOLATE_XY_POINTS:

      break;
    //State where if shit goes wrong, plotter is stopped and can be recovered from
    case EMERGENCY_STOP:

      break;
  }

}
