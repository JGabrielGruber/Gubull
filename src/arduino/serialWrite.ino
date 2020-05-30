#include <Servo.h>
#include "SPI.h"
#include "MFRC522.h"

String request;
boolean hello;
Servo servo;
String id;

const int pinRST = 9;
const int pinSDA = 10;

#define VERDE 2
#define AZUL 3
#define VERMELHO 4
#define SENSOR 6
#define SERVO 7


MFRC522 mfrc522(pinSDA, pinRST); 

void setup() {
	Serial.begin(9600);

	request = "";
	hello	= false;
	id		= "";

	pinMode(VERDE, OUTPUT);
	pinMode(AZUL, OUTPUT);
	pinMode(VERMELHO, OUTPUT);
	pinMode(SENSOR, INPUT);

	servo.attach(SERVO);

	SPI.begin();
	mfrc522.PCD_Init();

}

void loop() {
	request = Serial.read();
	if(getPeso()) {
		ctrlServo(false);
	}

	if (mfrc522.PICC_IsNewCardPresent() && id == "") {
		if(mfrc522.PICC_ReadCardSerial()) {
			for (byte i = 0; i < mfrc522.uid.size; ++i) {
				id	+= String(mfrc522.uid.uidByte[i]);
			}
		}
	}

	if (request != "-1") {
		if (!hello && request == "64") {
			delay(100); // OLÁ, O INICÍO DO PROTOCOLO
			setLed(1);
			Serial.print("@@");
			hello = true;
			delay(100);
		} else if (hello && request == "36" && id != "") {
			delay(100); // QUER O BRINCO
			setLed(1);
			Serial.print("$");
			Serial.print(id); // O BRINCO
			Serial.print("$");
		} else if (hello && request == "37" && getPeso()) {
			delay(100); // QUER O PESO
			setLed(1);
			Serial.print("%");
			Serial.print(getPeso()); // O PESO
			Serial.print("%");
		} else if (request == "33") {
			delay(100); // VISH, DEU MERDA
			setLed(4);
			hello = false;
			id = "";
			Serial.print("#");
		} else if (request == "114") {
			delay(100); // JÁ FOI PESADO HOJE
			setLed(3);
			hello = false;
			id = "";
			Serial.print("*");
			ctrlServo(true);
			delay(100);
		} else if (request == "111") {
			delay(100); // DEU BOA!
			setLed(2);
			hello = false;
			id = "";
			Serial.print("*");
			ctrlServo(true);
			delay(100);
			setLed(0);
		} else {
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

void setLed(int status) {
	if (status == 0) {
		digitalWrite(VERMELHO, HIGH);
		digitalWrite(AZUL, HIGH);
		digitalWrite(VERDE, HIGH);
	} else if (status == 1) {
		digitalWrite(VERMELHO, LOW);
		digitalWrite(AZUL, HIGH);
		digitalWrite(VERDE, LOW);
	} else if (status == 2) {
		digitalWrite(VERMELHO, LOW);
		digitalWrite(AZUL, LOW);
		digitalWrite(VERDE, HIGH);
	} else if (status == 3) {
		digitalWrite(VERMELHO, LOW);
		digitalWrite(AZUL, HIGH);
		digitalWrite(VERDE, HIGH);
	} else if (status == 4) {
		digitalWrite(VERMELHO, HIGH);
		digitalWrite(AZUL, LOW);
		digitalWrite(VERDE, LOW);
	}
}
