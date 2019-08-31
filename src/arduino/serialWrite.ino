String request;
boolean hello;

void setup() {
  Serial.begin(9600);
  request = "";
  hello  = false;
}

void loop() {
  request = Serial.read();
  if (request != "-1") {
    if (!hello && request == "64") {
      delay(100);
      Serial.print("@@");
      hello = true;
      delay(100);
  } else if (hello && request == "36") {
      delay(100);
      Serial.print("$");
      Serial.print(12345); // O BRINCO
      Serial.print("$");
  } else if (hello && request == "37") {
      delay(100);
      Serial.print("%");
      Serial.print(54.34); // O PESO
      Serial.print("%");
    } else if (request == "33"){
      hello = false;
      Serial.print("#");
    }
  }
}
