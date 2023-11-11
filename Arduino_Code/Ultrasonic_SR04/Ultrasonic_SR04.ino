#include <ENV.h>

long time;
int distance, distance_right, distance_left;

void setup() {
  Serial.begin(9600);
  pinMode(trig_right, OUTPUT);
  pinMode(echo_right, INPUT);
  pinMode(trig_left, OUTPUT);
  pinMode(echo_left, INPUT);
}

void calculate_distance(int trig, int echo) {
  digitalWrite(trig, LOW);
  delayMicroseconds(2);
  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);
  time = pulseIn(echo, HIGH);
  distance = time * c / 2;
  delay(200);
}

void loop() {
  calculate_distance(trig_right, echo_right);
  distance_right = distance;
  calculate_distance(trig_left, echo_left);
  distance_left = distance;
  if (DEBUG_MODE == "true") {
    Serial.print("distance_right : ");
    Serial.println(distance_right);
    Serial.print("distance_left : ");
    Serial.println(distance_left);
    Serial.println();
    delay(200);
  }
  if (distance_right < 10 && distance_left < 10 && distance_right != 0 && distance_left != 0) {
    Serial.println("Play/Pause");
  }
  else if (distance_right < 10 && distance_left > 10 && distance_right != 0) {
    Serial.println("Forward");
  }
  else if (distance_right > 10 && distance_left < 10 && distance_left != 0) {
    Serial.println("Backward");
  }
  delay(500);
}