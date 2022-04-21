SELECT scr_student_set.*, instructor_set.coh_ins_id, instructor_set.ifn, instructor_set.iln
FROM (SELECT scr.* , p.first_name as sfn, p.last_name as sln 
        FROM Student_Cohort_Registrations scr, People p 
        WHERE p.first_name = scr.student_id 
        AND p.first_name LIKE '%%' 
        OR p.last_name LIKE '%%') as scr_student_set
LEFT OUTER JOIN
(SELECT coh.cohort_id as coh_coh_id, coh.instructor_id as coh_ins_id, p.first_name as ifn, p.last_name as iln 
FROM People p, Cohorts coh
WHERE p.person_id = coh.instructor_id) as instructor_set
ON scr_student_set.cohort_id = instructor_set.coh_coh_id;