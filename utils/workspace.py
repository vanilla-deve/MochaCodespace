from pathlib import Path
from qt_compat import QTreeWidgetItem, Qt

def populate_tree(path: Path, tree_widget, max_depth=3, current_depth=0):
    """
    Populate a QTreeWidget with files/folders from path.
    `tree_widget` can be either the QTreeWidget itself (parent=None) or a QTreeWidgetItem parent.
    """
    if current_depth > max_depth:
        return

    try:
        entries = sorted(path.iterdir(), key=lambda p: (not p.is_dir(), p.name.lower()))
    except PermissionError:
        return

    for entry in entries:
        if entry.name.startswith('.'):
            continue
        if entry.name in ('__pycache__', 'node_modules', 'target', 'build', 'dist'):
            continue

        display_name = entry.name + ("/" if entry.is_dir() else "")

        if isinstance(tree_widget, type(tree_widget)):  # tree_widget is a QTreeWidget
            parent_item = QTreeWidgetItem(tree_widget, [display_name])
        else:
            # assume QTreeWidgetItem passed as parent
            parent_item = QTreeWidgetItem(tree_widget, [display_name])

        parent_item.setData(0, Qt.ItemDataRole.UserRole, str(entry))

        if entry.is_dir():
            try:
                populate_tree(entry, parent_item, max_depth, current_depth + 1)
            except Exception:
                # ignore permission errors on recursion
                pass
