#include <Arduino.h>

// Variabel fisika
float fx = 0, fy = 0, fz = 0;  // gaya
float ax = 0, ay = 0, az = 0;  // percepatan
float vx = 0, vy = 0, vz = 0;  // kecepatan
float x = 0, y = 0, z = 0;     // posisi
float mass = 1.0;              // massa benda (kg)
float dt = 0.1;                // interval waktu (s)

void setup() {
  delay(1000);
  Serial.begin(115200);
  Serial.println("x, y, z");
}

void loop() {
  // kontrol gaya
  if (Serial.available()) {
    char c = Serial.read();
    switch (c) {
      case 'w': fz += 1; break;  // dorong ke atas
      case 's': fz -= 1; break;  // dorong ke bawah
      case 'a': fx -= 1; break;  // kiri
      case 'd': fx += 1; break;  // kanan
      case 'q': fy += 1; break;  // maju
      case 'e': fy -= 1; break;  // mundur
      case 'r': fx = fy = fz = 0; break; // reset gaya
    }
  }

  // perhitungan
  ax = fx / mass;
  ay = fy / mass;
  az = fz / mass;

  vx += ax * dt;
  vy += ay * dt;
  vz += az * dt;

  x += vx * dt;
  y += vy * dt;
  z += vz * dt;

  // tampilan (x, y, z)
  Serial.print(x); Serial.print(",");
  Serial.print(y); Serial.print(",");
  Serial.println(z);

  delay(100);
}
