import grp
import pwd

PRIVILEGED_GROUPS = {'sudo', 'docker', 'lxd', 'libvirt', 'adm', 'wheel', 'root'}


def get_user_privileged_groups(username):
    """
    Busca a qué grupos privilegiados pertenece un usuario.
    Revisa tanto el grupo primario (GID) como los grupos secundarios (gr_mem).
    """
    user_groups = []
    
    # 1. Revisar grupo PRIMARIO (pw_gid en /etc/passwd)
    try:
        user_entry = pwd.getpwnam(username)
        primary_group = grp.getgrgid(user_entry.pw_gid)
        if primary_group.gr_name in PRIVILEGED_GROUPS:
            user_groups.append(primary_group.gr_name)
    except (KeyError, OSError):
        pass
    
    # 2. Revisar grupos SECUNDARIOS (gr_mem en /etc/group)
    all_groups = grp.getgrall()
    for group in all_groups:
        if group.gr_name in PRIVILEGED_GROUPS:
            if username in group.gr_mem:
                if group.gr_name not in user_groups:  # evitar duplicados
                    user_groups.append(group.gr_name)
    
    return user_groups


if __name__ == "__main__":
    import sys
    user = sys.argv[1] if len(sys.argv) > 1 else "eduar"
    print(f"Grupos privilegiados de {user}: {get_user_privileged_groups(user)}")
