SELECT
    *
from
    user;

SELECT
    *
from
    user u
    join address a on u.id = a.user_id
    ORDER BY u.id,a.id
    ;