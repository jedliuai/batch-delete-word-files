import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox, ttk


WORD_SUFFIXES = {".doc", ".docx"}


class WordCleanerApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("\u6279\u91cf\u5220\u9664 Word \u6587\u6863")
        self.root.geometry("900x600")

        self.folder_var = tk.StringVar()
        self.status_var = tk.StringVar(
            value="\u8bf7\u9009\u62e9\u8981\u626b\u63cf\u7684\u6587\u4ef6\u5939\u3002"
        )
        self.file_vars: list[tuple[Path, tk.BooleanVar]] = []

        self._build_ui()

    def _build_ui(self) -> None:
        container = ttk.Frame(self.root, padding=12)
        container.pack(fill=tk.BOTH, expand=True)

        top_frame = ttk.Frame(container)
        top_frame.pack(fill=tk.X)

        ttk.Label(top_frame, text="\u76ee\u6807\u6587\u4ef6\u5939:").pack(side=tk.LEFT)

        folder_entry = ttk.Entry(top_frame, textvariable=self.folder_var)
        folder_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(8, 8))

        ttk.Button(
            top_frame,
            text="\u9009\u62e9\u6587\u4ef6\u5939",
            command=self.choose_folder,
        ).pack(side=tk.LEFT)
        ttk.Button(
            top_frame,
            text="\u626b\u63cf Word \u6587\u6863",
            command=self.scan_files,
        ).pack(side=tk.LEFT, padx=(8, 0))

        action_frame = ttk.Frame(container)
        action_frame.pack(fill=tk.X, pady=(10, 10))

        ttk.Button(
            action_frame,
            text="\u5168\u9009",
            command=lambda: self.set_all(True),
        ).pack(side=tk.LEFT)
        ttk.Button(
            action_frame,
            text="\u5168\u90e8\u53d6\u6d88",
            command=lambda: self.set_all(False),
        ).pack(side=tk.LEFT, padx=(8, 0))
        ttk.Button(
            action_frame,
            text="\u6267\u884c\u5220\u9664",
            command=self.delete_selected,
        ).pack(side=tk.RIGHT)

        list_frame = ttk.Frame(container)
        list_frame.pack(fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(list_frame, highlightthickness=0)
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda event: self.canvas.configure(scrollregion=self.canvas.bbox("all")),
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        status_label = ttk.Label(container, textvariable=self.status_var, anchor="w")
        status_label.pack(fill=tk.X, pady=(10, 0))

    def choose_folder(self) -> None:
        selected = filedialog.askdirectory(
            title="\u9009\u62e9\u8981\u626b\u63cf\u7684\u6587\u4ef6\u5939"
        )
        if selected:
            self.folder_var.set(selected)

    def scan_files(self) -> None:
        folder_text = self.folder_var.get().strip()
        if not folder_text:
            messagebox.showwarning(
                "\u672a\u9009\u62e9\u6587\u4ef6\u5939",
                "\u8bf7\u5148\u9009\u62e9\u8981\u626b\u63cf\u7684\u6587\u4ef6\u5939\u3002",
            )
            return

        target_folder = Path(folder_text)
        if not target_folder.exists() or not target_folder.is_dir():
            messagebox.showerror(
                "\u6587\u4ef6\u5939\u65e0\u6548",
                "\u8bf7\u9009\u62e9\u4e00\u4e2a\u5b58\u5728\u7684\u6587\u4ef6\u5939\u3002",
            )
            return

        files = sorted(
            (path for path in target_folder.rglob("*") if path.is_file() and path.suffix.lower() in WORD_SUFFIXES),
            key=lambda item: str(item).lower(),
        )

        self._render_file_list(files)

        if files:
            self.status_var.set(
                f"\u5171\u627e\u5230 {len(files)} \u4e2a Word \u6587\u6863\uff0c"
                "\u9ed8\u8ba4\u5df2\u5168\u90e8\u9009\u4e2d\u3002"
            )
        else:
            self.status_var.set(
                "\u672a\u627e\u5230\u4efb\u4f55 .doc \u6216 .docx \u6587\u4ef6\u3002"
            )

    def _render_file_list(self, files: list[Path]) -> None:
        for child in self.scrollable_frame.winfo_children():
            child.destroy()

        self.file_vars.clear()

        for path in files:
            checked = tk.BooleanVar(value=True)
            relative_text = self._relative_display(path)
            checkbox = ttk.Checkbutton(
                self.scrollable_frame,
                text=relative_text,
                variable=checked,
            )
            checkbox.pack(fill=tk.X, anchor="w", pady=2)
            self.file_vars.append((path, checked))

    def _relative_display(self, path: Path) -> str:
        folder_text = self.folder_var.get().strip()
        try:
            return str(path.relative_to(folder_text))
        except ValueError:
            return str(path)

    def set_all(self, selected: bool) -> None:
        for _, var in self.file_vars:
            var.set(selected)

    def delete_selected(self) -> None:
        selected_files = [path for path, var in self.file_vars if var.get()]
        if not selected_files:
            messagebox.showinfo(
                "\u6ca1\u6709\u9009\u4e2d\u6587\u4ef6",
                "\u8bf7\u5148\u9009\u62e9\u81f3\u5c11\u4e00\u4e2a\u8981\u5220\u9664\u7684 "
                "Word \u6587\u6863\u3002",
            )
            return

        confirm = messagebox.askyesno(
            "\u786e\u8ba4\u5220\u9664",
            f"\u786e\u8ba4\u8981\u5220\u9664\u9009\u4e2d\u7684 {len(selected_files)} "
            "\u4e2a Word \u6587\u6863\u5417\uff1f\n"
            "\u5220\u9664\u540e\u65e0\u6cd5\u6062\u590d\u3002",
        )
        if not confirm:
            return

        deleted_count = 0
        failed: list[str] = []

        for path in selected_files:
            try:
                path.unlink()
                deleted_count += 1
            except Exception as exc:
                failed.append(f"{path}: {exc}")

        self.scan_files()

        if failed:
            preview = "\n".join(failed[:10])
            more = ""
            if len(failed) > 10:
                more = (
                    f"\n...... \u53e6\u6709 {len(failed) - 10} "
                    "\u4e2a\u6587\u4ef6\u5220\u9664\u5931\u8d25\u3002"
                )
            messagebox.showwarning(
                "\u5220\u9664\u5b8c\u6210",
                f"\u6210\u529f\u5220\u9664 {deleted_count} \u4e2a\u6587\u4ef6\uff0c"
                f"\u5931\u8d25 {len(failed)} \u4e2a\u3002\n\n{preview}{more}",
            )
            self.status_var.set(
                f"\u6210\u529f\u5220\u9664 {deleted_count} \u4e2a\u6587\u4ef6\uff0c"
                f"\u5931\u8d25 {len(failed)} \u4e2a\u3002"
            )
            return

        messagebox.showinfo(
            "\u5220\u9664\u5b8c\u6210",
            f"\u6210\u529f\u5220\u9664 {deleted_count} \u4e2a Word \u6587\u6863\u3002",
        )
        self.status_var.set(
            f"\u6210\u529f\u5220\u9664 {deleted_count} \u4e2a Word \u6587\u6863\u3002"
        )


def main() -> None:
    root = tk.Tk()
    app = WordCleanerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
