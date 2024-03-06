import { createClient, print } from "redis";

const redis = createClient();

redis
  .on("connect", () => {
    console.log("Redis redis connected to the server");
  })
  .on("error", (error) => {
    console.log(`Redis redis not connected to the server: ${error}`);
  });

redis.hset('HolbertonSchools', 'Portland', '50', print);
redis.hset('HolbertonSchools', 'Seattle', '80', print);
redis.hset('HolbertonSchools', 'New York', '20', print);
redis.hset('HolbertonSchools', 'Bogota', '20', print);
redis.hset('HolbertonSchools', 'Cali', '40', print);
redis.hset('HolbertonSchools', 'Paris', '2', print);

redis.hgetall('HolbertonSchools', (error, result) => {
    if (error) {
        console.log(error);
        throw error;
    }
    console.log(result);
});
