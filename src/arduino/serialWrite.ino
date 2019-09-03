#include <Servo.h>

String request;
boolean hello;
Servo servo;

#define VERDE 2
#define AZUL 3
#define VERMELHO 4
#define SENSOR 6
#define SERVO 7

void setup() {
	Serial.begin(9600);

	request = "";
	hello	= false;

	pinMode(VERDE, OUTPUT);
	pinMode(AZUL, OUTPUT);
	pinMode(VERMELHO, OUTPUT);
	pinMode(SENSOR, INPUT);

	servo.attach(SERVO);
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
			Serial.print(getBrinco()); // O BRINCO
			Serial.print("$");
		} else if (hello && request == "37") {
			delay(100);
			Serial.print("%");
			Serial.print(getPeso()); // O PESO
			Serial.print("%");
		} else if (request == "33") {
			hello = false;
			Serial.print("#");
		}
	}
}

void ctrlServo(boolean aberto) {
	if (aberto) {
		servo.write(0);
	} else {
		servo.write(90);
	}
}

float getPeso() {
	if (digitalRead(SENSOR)) {
		return random(200, 500);
	} else {
		return 0.0;
	}
}

String getBrinco() {
	if (true) {
		return "12435231312";
	} else {
		return "";
	}
	
}
