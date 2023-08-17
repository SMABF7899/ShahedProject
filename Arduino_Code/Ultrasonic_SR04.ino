int trig = 7;
int echo = 6;
float time;
int C = 343; //Speed ​​of sound [m/s]
float distance;

void setup() {
  Serial.begin(9600);
  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);
}

void loop() {
  digitalWrite(trig, LOW);
  delayMicroseconds(2000);
  digitalWrite(trig, HIGH);
  delayMicroseconds(15);
  digitalWrite(trig, LOW);
  delayMicroseconds(10);
  time = pulseIn(echo, HIGH);
  time = time / 1000000;
  distance = C * time * 100;
  Serial.println(distance);
  delay(200);
}
