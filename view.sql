-- Join tbl_MedDatarisk with personIDs
CREATE VIEW django_studentanalytics.studentrisk_student AS
SELECT
  a.*,
  b.email,
  b.fullName,
  c.name campusName,
  d.ramme_retning,
  d.fra_dato,
  d.til_dato,
  d.adgangsgrundlag,
  d.udmeld_aarsag,
  d.udmeld_begrundelse
FROM
  tbl_MedDatarisk AS a
LEFT OUTER JOIN
  map_personIDs AS b ON a.studienr = b.studienr
LEFT OUTER JOIN
  tbl_campi AS c ON a.CourseLocation = c.tbl_campiID
LEFT OUTER JOIN
  tbl_optag AS d ON a.studienr = d.studienr

-- Create a view of tbl_predictors
CREATE VIEW django_studentanalytics.studentrisk_predictors AS
SELECT
  a.*,
  b.*,
  c.Name source,
  d.dateRun
FROM
  tbl_predictors AS a
LEFT OUTER JOIN
  tbl_logreg_models AS b ON a.`Pred ID` = b.`Pred.ID`
LEFT OUTER JOIN
  tbl_predictorTypes AS c ON a.`predictoryTypeID` = c.`predictoryTypeID`
LEFT OUTER JOIN
  tbl_models AS d ON b.`modelID` = d.`modelID`