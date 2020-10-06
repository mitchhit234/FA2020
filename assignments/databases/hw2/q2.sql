-- Selected all columns, if you just wanted the names of the art
-- you would replace SELECT * with SELECT mdmfvz.ART.NAME

SELECT *
FROM mdmfvz.ART
LEFT JOIN mdmfvz.ORIGIN
ON mdmfvz.ART.ORIGIN_ID = mdmfvz.ORIGIN.ORIGIN_ID
ORDER BY mdmfvz.ORIGIN.LOCATION, mdmfvz.ART.NAME;