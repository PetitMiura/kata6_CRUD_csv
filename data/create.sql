CREATE TABLE "movements" (
	"id"	INTEGER UNIQUE,
	"date"	TEXT NOT NULL,
	"abstract"	INTEGER NOT NULL,
	"amount"	REAL NOT NULL,
	"currency"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);


CREATE INDEX "ix_currency_amount" ON "movements" (
	"currency"	ASC,
	"amount"	DESC
)