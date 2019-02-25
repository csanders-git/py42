from ..authoritybase import AuthorityTargetedClient


class BackupRestoreClient(AuthorityTargetedClient):

    def get_restore_history(self, days, org_id=None, page_num=None, page_size=None, **kwargs):
        uri = "/api/RestoreHistory"
        params = {"days": days, "orgId": org_id, "pgNum": page_num, "pgSize": page_size}
        return self.get(uri, params=params, **kwargs)
