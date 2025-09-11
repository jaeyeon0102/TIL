USE online_course_platform_db

SELECT 
  s.username,
  c.title AS course_title,
  f.created_at
FROM feedback f
INNER JOIN students s
  ON f.student_id = s.id
INNER JOIN courses c 
  ON f.course_id = c.id 
WHERE s.username = 'john_doe';


SELECT 
  s.username,
  c.title AS course_title,
  f.comment
FROM feedback f
LEFT JOIN courses c
  ON f.course_id = c.id
LEFT JOIN students s
  ON f.student_id = s.id
WHERE s.username = 'jane_smith';


SELECT 
  f.comment 
FROM feedback f
WHERE f.student_id = (
  SELECT id 
  FROM students s
  WHERE s.username = 'mary_jones'
)
