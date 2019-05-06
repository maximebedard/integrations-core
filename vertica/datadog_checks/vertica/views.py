# (C) Datadog, Inc. 2019
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

# System tables:
# https://www.vertica.com/docs/9.2.x/HTML/Content/Authoring/AdministratorsGuide/Monitoring/Vertica/UsingSystemTables.htm
# https://www.vertica.com/docs/9.2.x/HTML/Content/Authoring/SQLReferenceManual/SystemTables/VerticaSystemTables.htm


class View(object):
    name = ''

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        if isinstance(other, View):
            return self.name == other.name

        return self.name == other

    # TODO: Remove when only on Python 3+
    def __ne__(self, other):
        return not self == other


class Licenses(View):
    """
    https://www.vertica.com/docs/9.2.x/HTML/Content/Authoring/SQLReferenceManual/SystemTables/CATALOG/LICENSES.htm
    """

    name = 'licenses'
    fields = ('end_date', 'name', 'node_restriction')
    query = 'SELECT {} FROM v_catalog.{}'.format(', '.join(fields), name)


class LicenseAudits(View):
    """
    https://www.vertica.com/docs/9.2.x/HTML/Content/Authoring/SQLReferenceManual/SystemTables/CATALOG/LICENSE_AUDITS.htm
    """

    name = 'license_audits'
    fields = ('audit_start_timestamp', 'database_size_bytes', 'license_size_bytes')
    query = (
        "SELECT {} FROM v_catalog.{} WHERE audited_data = 'Total' "
        "ORDER BY audit_start_timestamp DESC LIMIT 1".format(', '.join(fields), name)
    )


class Nodes(View):
    """
    https://www.vertica.com/docs/9.2.x/HTML/Content/Authoring/SQLReferenceManual/SystemTables/CATALOG/NODES.htm
    """

    name = 'nodes'
    fields = ('node_name', 'node_state')
    query = 'SELECT {} FROM v_catalog.{}'.format(', '.join(fields), name)


class Projections(View):
    """
    https://www.vertica.com/docs/9.2.x/HTML/Content/Authoring/SQLReferenceManual/SystemTables/CATALOG/PROJECTIONS.htm
    """

    name = 'projections'
    fields = ('is_segmented', 'is_up_to_date')
    query = 'SELECT {} FROM v_catalog.{}'.format(', '.join(fields), name)


class ProjectionStorage(View):
    """
    https://www.vertica.com/docs/9.2.x/HTML/Content/Authoring/SQLReferenceManual/SystemTables/MONITOR/PROJECTION_STORAGE.htm
    """

    name = 'projection_storage'
    fields = ('anchor_table_name', 'node_name', 'projection_name', 'ros_row_count', 'used_bytes', 'wos_row_count')
    query = 'SELECT {} FROM v_monitor.{}'.format(', '.join(fields), name)
