// Define the pins for the ULPSM-CO 968-001 sensor
#define VREF_PIN A0
#define VGAS_PIN A1
#define VTEMP_PIN A2


// Define the resistance of the load resistor in ohms
#define LOAD_RESISTOR 10000

void setup() {

  Serial.begin(9600);

}

void loop() {
  // Read the analog voltages from the sensor pins
  float v_ref = analogRead(VREF_PIN) * (3.3 / 1023.0);
  float v_gas = analogRead(VGAS_PIN) * (3.3 / 1023.0);
  float v_temp = analogRead(VTEMP_PIN) * (3.3 / 1023.0);

  // Calculate the resistance of the sensor
  float r_gas = ((3.3 - v_gas) * LOAD_RESISTOR) / v_gas;

  // Calculate the concentration level of CO in ppm
  float co_concentration = ((r_gas / 5000.0) + 0.01);
  delay(500);

  // Print the CO concentration to the serial monitor
  Serial.println(co_concentration);
}
 
