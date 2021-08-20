class Sql:
    userlist = "SELECT * FROM users";
    userlistone = "SELECT * FROM users WHERE user_id= '%s' ";
    userinsert = "INSERT INTO users VALUES ('%s','%s','%s','%s','%s',CURRENT_DATE())";
    userdelete = "DELETE FROM users WHERE user_id= '%s' ";
    userupdate = "UPDATE users SET pwd='%s',name='%s',email='%s',phone='%s' WHERE user_id= '%s' ";

    udatalist = """ SELECT * FROM udata
                    """;
    udatalistone = "SELECT * FROM udata WHERE id= '%s' ";
    udatainsert = """INSERT INTO udata VALUES
                        (NULL,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',CURRENT_DATE())""";
    udatadelete = "DELETE FROM udata WHERE id= '%s' ";
    udataupdate = """UPDATE udata SET schooltype='%s', majorcate='%s', age='%s', intern='%s',
                                toeic='%s',tosp='%s', train='%s', jobseek='%s',
                                cert='%s',jobsearch='%s', yrwish='%s', wishhr='%s',
                                wishsalary='%s', jobgradu='%s',liveexp='%s'
                          WHERE id= '%s'
                      """;

    resultlist = """ SELECT * FROM res WHERE id= '%s' """;
    resultinsert = "INSERT INTO res VALUES (NULL, '%s', '%s', CURRENT_DATE())";
