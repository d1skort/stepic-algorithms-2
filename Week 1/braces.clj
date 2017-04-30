(ns braces)

(def braces #{\( \) \{ \} \[ \]})

(def pairs { \) \(,
             \} \{,
             \] \[})

(defn balanced?
  [string]
  (loop [[part & remaining] string
         stack (list)
         i 1]
    (if (contains? braces part)
      (if (pairs part) (if (= (pairs part) (:brace (peek stack)))
                         (recur remaining (pop stack) (inc i))
                         i)
        (recur remaining (conj stack {:brace part :idx i}) (inc i)))
      (if (nil? part)
        (if (empty? stack)
          "Success"
          (:idx (peek stack)))
        (recur remaining stack (inc i))))))

(defn main
  [& args]
  (println (balanced? (read-line))))

(main)
