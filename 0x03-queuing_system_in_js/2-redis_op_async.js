import { promisify } from 'util';
import { createClient, print } from "redis";

const redis = createClient();
redis
  .on("error", (err) =>
    console.log("Redis client not connected to the server: ", err)
  )
  .on("connect", () => {
    console.log("Redis client connected to the server");
  });

  function setNewSchool(schoolName, value) {
  redis.set(schoolName, value, print);
}

async function displaySchoolValue(schoolName) {
  console.log(await promisify(redis.GET).bind(redis)(schoolName));
};

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");
