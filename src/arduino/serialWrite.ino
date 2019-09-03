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

	setLed(0);
}

void loop() {
	request = Serial.read();
	if(getPeso()) {
		ctrlServo(false);
	}
	if (request != "-1") {
		if (!hello && request == "64") {
			setLed(1);
			delay(100); // OLÁ, O INICÍO DO PROTOCOLO
			Serial.print("@@");
			hello = true;
			delay(100);
		} else if (hello && request == "36") {
			setLed(1);
			delay(100); // QUER O BRINCO
			Serial.print("$");
			Serial.print(getBrinco()); // O BRINCO
			Serial.print("$");
		} else if (hello && request == "37") {
			setLed(1);
			delay(100); // QUER O PESO
			Serial.print("%");
			Serial.print(getPeso()); // O PESO
			Serial.print("%");
		} else if (request == "33") {
			setLed(4);
			delay(100); // VISH, DEU MERDA
			hello = false;
			Serial.print("#");
		} else if (request == "114") {
			setLed(3);
			delay(100); // JÁ FOI PESADO HOJE
			hello = false;
			Serial.print("*");
			ctrlServo(true);
			delay(1000);
		} else if (request == "111") {
			setLed(2);
			delay(100); // DEU BOA!
			hello = false;
			Serial.print("*");
			ctrlServo(true);
			delay(5000);
		} else {
			setLed(0);
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

void setLed(int status) {
	switch (status) {
		case 0:
			serialWrite(VERMELHO, HIGH);
			serialWrite(AZUL, HIGH);
			serialWrite(VERDE, HIGH);
		case 1:
			serialWrite(VERMELHO, LOW);
			serialWrite(AZUL, HIGH);
			serialWrite(VERDE, LOW);
		case 2:
			serialWrite(VERMELHO, LOW);
			serialWrite(AZUL, LOW);
			serialWrite(VERDE, HIGH);
		case 3:
			serialWrite(VERMELHO, LOW);
			serialWrite(AZUL, HIGH);
			serialWrite(VERDE, HIGH);
		case 4:
			serialWrite(VERMELHO, HIGH);
			serialWrite(AZUL, LOW);
			serialWrite(VERDE, LOW);
	}
}
