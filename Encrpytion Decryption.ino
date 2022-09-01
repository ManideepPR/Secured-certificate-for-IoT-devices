#include <Crypto.h>
#include <Speck.h>
#include <SpeckSmall.h>
#include <SpeckTiny.h>
#include <string.h>

unsigned long startTime;
unsigned long lastYield = 0;
bool useRNG =true;

int randomBitRaw(void){
  if(lastYield ==0 || millis() - lastYield>=50){
    yield();
    lastYield = millis();
  }
  uint8_t bit = analogRead(A0);
  return bit & 1;
}

int randomBitRaw2(void) {
  for(;;) {
    int a = randomBitRaw() | (randomBitRaw()<<1);
    if (a==1) return 0; // 1 to 0 transition: log a zero bit
    if (a==2) return 1; // 0 to 1 transition: log a one bit
  }
  return 0;
}
byte *randomBitRaw3(){
  static byte r[128];
  for(int i=0;i<128;i++){
    r[i] = randomBitRaw2();
  }
  return r;
}
struct TestVector
{
    const char *name;
    byte key[32];
    byte plaintext[16];
    byte ciphertext[16];
};

static TestVector const testVectorSpeck128 = {
    .name        = "Speck-128-ECB",
    .plaintext   = {"hello"}
};

Speck speck;

byte buffer[16];

void testCipher(BlockCipher *cipher, const struct TestVector *test, size_t keySize, bool decryption = true)
{
    byte encr[16];
    byte decr[16];
    unsigned long start;
    unsigned long elapsed;
    byte *key;
    key = randomBitRaw3();
    Serial.println("Secret Key:");
    for(int i =0;i<128;i++){
      Serial.print(key[i],HEX);
    }
    Serial.println();
    start = micros();
    cipher->setKey(key, keySize);
    elapsed = micros()-start;
    Serial.println("Set key");
    Serial.print(elapsed);
    Serial.print("us per operation, ");
    Serial.print((1000000.0) / elapsed);
    Serial.println(" bytes per second");
    start = micros();
    cipher->encryptBlock(encr, test->plaintext);
    elapsed = micros()-start;
    Serial.print("\nAfter Encrypting\n");
    for(int i=0;i<sizeof(encr);i++){
      Serial.print(encr[i],HEX);
    }
    Serial.println();
    Serial.print(elapsed / (16.0));
    Serial.print("us per byte, ");
    Serial.print((16.0 *1000000.0) / elapsed);
    Serial.println(" bytes per second");

    /*if (memcmp(buffer, test->ciphertext, 16) == 0)
        Serial.print("Passed");
    else
        Serial.print("Failed");
*/
    if (!decryption)
        return;

    //Serial.print(" Decryption ... ");
    start=micros();
    cipher->decryptBlock(decr, encr);
    elapsed = micros() - start;
    Serial.print("\nAfter Decrypting\n");
    for(int i = 0 ; i < sizeof(decr) ; i++){
      Serial.print(decr[i],HEX);
    }
    Serial.println();
    Serial.print(elapsed / (16.0));
    Serial.print("us per byte, ");
    Serial.print((16.0 * 1000000.0) / elapsed);
    Serial.println(" bytes per second");
    Serial.println();
}

void setup()
{
    Serial.begin(9600);
    Serial.println();
}

void loop()
{
  testCipher(&speck, &testVectorSpeck128, 16);
  delay(5000);
}
