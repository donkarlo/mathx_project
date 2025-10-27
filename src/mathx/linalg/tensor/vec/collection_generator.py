from pathlib import Path
from typing import Generic, TypeVar, Type, List
from mathx.linalg.tensor.vec.vec import Vec
from utilix.data.storage.type.file.file import File

VecType = TypeVar("VecType", bound=Vec)


class CollectionGenerator(Generic[VecType]):

    @staticmethod
    def generate_list_from_file_path(cls: Type[VecType], file_path: str, vec_sep: str = "\n",
                                     component_sep: str = " ") -> List[VecType]:
        path = Path(file_path)
        text = File(path).get_ram().strip()

        vecs: List[VecType] = []
        factory = getattr(cls, "init_from_components", None)  # optional hook
        for rec in text.split(vec_sep):
            line = rec.strip()
            if not line:
                continue
            comps = [float(c) for c in line.split(component_sep) if c]
            # type: ignore[arg-type]
            obj = factory(comps) if callable(factory) else cls(comps)
            vecs.append(obj)
        return vecs
