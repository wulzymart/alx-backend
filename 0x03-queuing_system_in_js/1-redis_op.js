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

function displaySchoolValue(schoolName) {
  redis.get(schoolName, (error, result) => {
    if (error) {
      console.log(error);
      throw error;
    }
    console.log(result);
  });
}

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");
