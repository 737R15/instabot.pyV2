CREATE TABLE "usernames_new" ( `username_id` varchar ( 300 ), `username` TEXT  );
INSERT INTO "usernames_new" (username_id) Select username from usernames;
DROP TABLE "usernames";
ALTER TABLE "usernames_new" RENAME TO "usernames";